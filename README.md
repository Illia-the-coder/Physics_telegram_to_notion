# 📝 Readme

## 🔎 Introduction

Have you ever wanted to analyze your group chat history in a structured and easy-to-read format? This code is here to help! Written in Python, this code processes the exported history of a Telegram group chat and creates telegraph pages with the images. Additionally, it matches the dates from the processed data with the dates from the plans files to give you an overview of how the actual lessons align with the planned lessons.

## 💻 Technical Details

The code uses the following libraries for its processing:

| Library | Purpose |
|---------|---------|
| Numpy | For linear algebra |
| Pandas | For data processing and working with CSV files |
| JSON | For reading JSON data |

It processes two sets of data: 'result.json' and two plans files, '7_plan.csv' and '8_plan.csv'. The code reads the 'result.json' file and stores it in a pandas DataFrame 'df'. The 'date' column is transformed into a readable format by the PC and the 'serv' column is added to the DataFrame with the URL of the uploaded image. The DataFrame is then sorted into two DataFrames 's_g' and 'e_g' based on dates.

## 🎨 Creation of Telegraph Pages

The code then groups the 's_g' DataFrame by date and creates a telegraph page for each group with the images of that group. The date, date in a readable format, and the link to the telegraph page are stored in a DataFrame 'res_s'.

The same steps are repeated for the 'e_g' DataFrame and the results are saved in a DataFrame 'res_e'.

## 📅 Matching with Plan

Finally, the code matches the dates from the 'res_s' and 'res_e' DataFrames with the dates from the plans files, '7_plan.csv' and '8_plan.csv', respectively. The transformed data is then saved for further analysis.

## 🏁 Conclusion

With these steps, you can now easily analyze and visualize the information from your group chat history. Whether you're a teacher looking to track your lessons or just a member of a group chat looking to reminisce, this code provides a clean and structured way to do so. 🎉
Also I posted all this structured info in notion page and then in super page - https://physics171.super.site/
![image](https://user-images.githubusercontent.com/101904816/230796282-a76307cd-568d-493d-8f57-14ca2eb82d51.png)
