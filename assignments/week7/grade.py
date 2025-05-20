import csv
import random
import statistics
import pandas as pd


file_path = "Technical_Basics_I_2025_Sheet1.csv"
output_path = "Technical_Basics_update.csv"


week_columns = [f"week{i}" for i in range(1, 14) if i != 6]
max_total_points = 30

try:

    with open(file_path, newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        original_fields = reader.fieldnames or []

        for week in week_columns:
            if week not in original_fields:
                original_fields.append(week)

        fieldnames = original_fields + ["Total Points", "Average Points"]
        students = []

        for row in reader:
            scores = []

            for week in week_columns:
                val = row.get(week, "")
                if val is None:
                    val = ""
                val = val.strip()

                if val == "" or val == "-" or val.lower() == "nan":
                    score = round(random.uniform(0, 3), 1)
                    row[week] = str(score)
                    scores.append(score)
                else:
                    try:
                        score = float(val)
                        scores.append(score)
                    except ValueError:
                        row[week] = "0.0"
                        scores.append(0.0)

            avg = round(statistics.mean(scores), 2) if scores else 0.0
            top_10 = sorted(scores, reverse=True)[:10]
            total = min(round(sum(top_10), 2), max_total_points)

            row["Average Points"] = avg
            row["Total Points"] = total

            students.append(row)

    with open(output_path, "w", newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

    print(f"finish to make: {output_path}\n")

    df = pd.read_csv(output_path)

    print("Average Points by Stream:")
    if "Stream" in df.columns:
        stream_a = df[df["Stream"].str.upper() == "A"]
        stream_b = df[df["Stream"].str.upper() == "B"]
        print(f" Stream A: {round(stream_a['Average Points'].mean(), 2)}")
        print(f" Stream B: {round(stream_b['Average Points'].mean(), 2)}")

    print("\nWeekly Average Points:")
    for week in week_columns:
        if week in df.columns:
            avg = round(df[week].astype(float).mean(), 2)
            print(f"  {week.capitalize():<6}: {avg}")

except FileNotFoundError:
    print("Can't find CSV file. Check the file name.")
except Exception as e:
    print(f"exception : {e}")
