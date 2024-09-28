import threading
import os, subprocess, sys, signal, atexit

# Initiate global variables
ROOT = os.geteuid() == 0
UP = 1
DOWN = 0
rtmp_status = DOWN
pid_map = {}
NUMBER_OF_EXPERIMENTS = 5

def safely_end():
        terminate(*pid_map.keys())

# Defining thread functions
def terminate(*args):
        global pid_map
        for process in args:
                try:
                        os.kill(pid_map[process], signal.SIGTERM)
                        print('Sending SIGTERM for', process)
                except ProcessLookupError:
                        print(process, 'already terminated.')
                pid_map.pop(process, None)

def server_up():
        global rtmp_status, pid_map

        command = "docker-compose up --build"
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        pid_map["rtmp_server"] = process.pid

        while rtmp_status == DOWN:
                output = process.stdout.readline()
                if output:
                        line = output.decode().strip()
                        print(line)
                        words_in_line = line.split()

                if (output and len(words_in_line) > 0 and (words_in_line[0] == 'Successfully' or words_in_line[0] == 'Attaching')):
                        os.system("sleep 0.5")
                        rtmp_status = UP

        while rtmp_status == UP:
                continue

def stream_video():
        global rtmp_status
        command = "ffmpeg -re -i ./video-test.mp4 -c:v  libx264 -c:a aac -f flv rtmp://localhost/hls"

        while rtmp_status == DOWN:
                continue

        process = subprocess.Popen(command.split())
        pid_map['ffmpeg'] = process.pid

def start_test():
        global rtmp_status, pid_map

        for i in range(1, NUMBER_OF_EXPERIMENTS + 1):
                os.system('sleep 1')
                stream_video()
                print(f"\n\n\033[31;1;4mEXPERIMENTO {i}\033[0m\n\n")
                os.system(f'./generate_report.sh {i}')
                terminate('ffmpeg')
                print(f"\n\nEXPERIMENTO {i} FINALIZADO\n\n")

        rtmp_status = DOWN
        safely_end()



if __name__ == "__main__":
        if not ROOT:
                print("Script must be executed as superuser (root).")
                sys.exit(1)

        atexit.register(safely_end)

        # Initiatin threads
        threads = [
                threading.Thread( target = server_up ),
        ]


        for t in threads:
                t.start()

        start_test()
