grep -v '^#' ms_data_dirty.csv | sed '/^$/d' | sed 's/,,*/,/g' | \
cut -d',' -f1,2,4,5,6 | \
awk -F',' '{if (NR==1 || ($5 >= 2.0 && $5 <= 8.0)) print}' > ms_data.csv
echo -e "insurance_type\nBasic\nPremium\nPlatinum" > insurance.lst
total_visits=$(tail -n +2 ms_data.csv | wc -l)
echo "Total number of visits: $total_visits"
echo "First few records:"
head -n 8 ms_data.csv