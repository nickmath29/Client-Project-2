# Open the CSV file and extract the data
with open(csv_file, newline='', encoding='utf-8') as file:
   reader = csv.reader(file)
   data = list(reader)


# Extract the data from the CSV
meet_name = data[1][0]  # Column A - h1 (Meet Name)
meet_date = data[1][1]  # Column B - h2 (Meet Date)
team_results_link = data[1][2]  # Column C - hyperlink for the team-results section
folder_name = data[1][3]  # Column D - folder name used in photo-gallery links
race_comments = data[1][4]  # Column E - race-comments section


# print(f"meet name {meet_name}")
# print(f"meet_date {meet_date}")
# print(f"folder_name {folder_name}")
# print(f"race_comments{race_comments}")


# Athlete details start from row 2 (index 1)
athletes = data[1:]


# Start building the HTML structure
html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <link rel = "stylesheet" href = "css/reset.css">
   <link rel = "stylesheet" href = "css/style.css">
   <title>{meet_name} Country Meet</title>
</head>
<body>


   <header>
       <h1>{meet_name}</h1>
       <h2>{meet_date}</h2>
   </header>
   
</body>