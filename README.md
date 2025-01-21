Second Practice Project: Data Cleaning with Pandas

This project marks my second attempt at data cleaning using Pandas, and while I still hadn’t learned matplotlib, I relied on colorama once again for visualization. 
At first glance, you can immediately notice an improvement in the structure of the code:
The code is cleaner, better organized, and includes comments to guide the reader.

Key Improvements

As I mentioned before, it’s essential to have a clear purpose for your data cleaning process and remove unnecessary information. 
In this project, that principle was followed much more closely, and extra columns were dropped using drop().

What’s the Main Educational Highlight?

Even though the project is more readable and visually structured, it’s still similar to the first one. So, what makes it unique? Just cleanliness?
The main learning point lies between lines 20 to 27, where I converted the Income column from an object to an integer.
Specifically :

Removed the $ symbol from values.

Retained only the numerical part.
In simpler terms:
$10 → 10

But that’s not all! 
A few lines earlier, lines 16 to 18, I tackled missing values in the Country column.
Some individuals didn’t have a country listed (i.e., NaN values). Instead of deleting those rows entirely, I replaced them with the term Traveler, assuming they could represent people who are always on the move. 

Output

The output format remains consistent with the previous project:
1️⃣ First, it displays the cleaned dataset.
2️⃣ Then, using colorama, it answers a few questions:

Blue: Most frequent gender.

Green: Most common job.

Light Blue: Company with the highest number of employees.

Pink: Country with the largest population in the dataset.

Yellow: Highest income.
