# DATA PIPELINE DEVELOPMENT

*COMPANY NAME* : CODETECH IT SOLUTIONS

*NAME*         : MEGAA C V

*INTERN ID*    : CT06DN683

*DOMAIN*       : DATA SCIENCE

*DURATION*     : 6 WEEKS

*MENTOR*       : NEELA SANTHOSH

# Description of my task

My first task was to design and implement an automated ETL (Extract, Transform, Load) pipeline using Python. The goal was to create a user-friendly script that accepts any CSV dataset, cleans and transforms the data, and exports the refined dataset for analysis.

The pipeline starts with extracting data by prompting the user for the dataset path, validating the file, and reading it through the Pandas library. 

In the transformation phase, I addressed common issues like missing data and inconsistent formats. For numerical columns, I imputed missing values using the median, while for categorical columns, I replaced missing values with “Unknown” to maintain data integrity. I also applied Label Encoding to convert categorical variables into numerical formats and used StandardScaler from Scikit-learn to scale numerical columns.

Finally, the cleaned dataset is saved as a new CSV file in the same directory as the original. The script features clear prompts, status messages, and error handling, making it beginner-friendly and ready for production.

Overall, this ETL pipeline streamlines an essential part of the data science workflow, ensuring datasets are clean and analysis-ready before modeling.

# OUTPUT
[cleaned_data.csv](https://github.com/user-attachments/files/20347774/cleaned_data.csv)

![Image](https://github.com/user-attachments/assets/1d4cef46-6cee-4622-bab3-66760b35f351)
