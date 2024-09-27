#!/bin/bash

number=$1
report_path="./reports"

mkdir -p $report_path

> $report_path/experiment-$number.txt

ps -o 'pid %cpu %mem stat cputimes etime command' -c | head -n 1 >> $report_path/experiment-$number.txt

for i in {0..25}; do
        ps -o 'pid %cpu %mem stat cputimes etime command' -c | grep 'ffmpeg' | head -n 1 >> $report_path/experiment-$number.txt
        sleep 1
done

if [[ $number -eq 1 ]]; then
        header="0s"
        for i in {1..25}; do
                header+=",${i}s"
        done
        echo $header > $report_path/cpu.csv
        echo $header > $report_path/mem.csv
        echo $header > $report_path/cpu-time.csv
fi

echo $(cat $report_path/experiment-$number.txt | tail -n +2 | awk '{print $2}' | tr "\n" "," | sed 's/.$//') >> $report_path/cpu.csv
echo $(cat $report_path/experiment-$number.txt | tail -n +2 | awk '{print $3}' | tr "\n" "," | sed 's/.$//') >> $report_path/mem.csv
echo $(cat $report_path/experiment-$number.txt | tail -n +2 | awk '{print $5}' | tr "\n" "," | sed 's/.$//') >> $report_path/cpu-time.csv
