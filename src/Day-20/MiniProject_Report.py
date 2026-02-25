from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted
from reportlab.lib.styles import getSampleStyleSheet

# Create PDF
doc = SimpleDocTemplate("Customer_Analytics_Code_Documentation.pdf")
styles = getSampleStyleSheet()

content = []

# -------------------------------
# TITLE
# -------------------------------
content.append(Paragraph("Customer Analytics Project: Source Code Documentation", styles["Title"]))
content.append(Spacer(1, 12))

content.append(Paragraph(
    "This document contains the source code and technical explanation for the Customer Analytics Exploratory Data Analysis (EDA) project. "
    "The report covers data inspection, preprocessing, visualization, and analysis steps performed using Python libraries such as Pandas, Matplotlib, and Seaborn.",
    styles["Normal"]
))
content.append(Spacer(1, 20))

# -------------------------------
# TABLE OF CONTENTS
# -------------------------------
content.append(Paragraph("Table of Contents", styles["Heading2"]))
content.append(Paragraph(
    "1. Exploratory Data Analysis Notebook<br/>"
    "2. Data Cleaning and Preprocessing<br/>"
    "3. Data Visualization<br/>"
    "4. Correlation Analysis<br/>"
    "5. Analysis and Insights",
    styles["Normal"]
))
content.append(Spacer(1, 20))

# -------------------------------
# SECTION 1
# -------------------------------
content.append(Paragraph("1. Exploratory Data Analysis Notebook", styles["Heading2"]))

content.append(Paragraph(
    "The notebook performs a structured exploratory data analysis workflow including data loading, inspection, preprocessing, and visualization. "
    "The dataset is analyzed using Python to understand its structure and derive meaningful insights.",
    styles["Normal"]
))
content.append(Spacer(1, 12))

content.append(Paragraph(
    "The head(), info(), and describe() functions are used to explore the dataset. These functions help in understanding column names, "
    "data types, missing values, and statistical summaries such as mean, standard deviation, minimum, and maximum values.",
    styles["Normal"]
))
content.append(Spacer(1, 12))

code1 = """
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("customer_data.csv")

df.head()
df.info()
df.describe()
"""
content.append(Preformatted(code1, styles["Code"]))
content.append(Spacer(1, 20))

# -------------------------------
# SECTION 2
# -------------------------------
content.append(Paragraph("2. Data Cleaning and Preprocessing", styles["Heading2"]))

content.append(Paragraph(
    "Data cleaning is a crucial step in data analysis. Real-world datasets often contain missing values and duplicate records "
    "which can negatively affect analysis results if not handled properly.",
    styles["Normal"]
))
content.append(Spacer(1, 12))

content.append(Paragraph(
    "Missing values in the 'AnnualIncome' column were filled using mean imputation to maintain numerical consistency. "
    "For the 'Education' column, missing values were replaced using the mode since it represents the most frequent category.",
    styles["Normal"]
))
content.append(Spacer(1, 12))

content.append(Paragraph(
    "Duplicate rows were identified and removed to ensure data accuracy and avoid redundancy. "
    "These preprocessing steps improve the overall quality of the dataset.",
    styles["Normal"]
))
content.append(Spacer(1, 12))

code2 = """
df["AnnualIncome"] = df["AnnualIncome"].fillna(df["AnnualIncome"].mean())
df["Education"] = df["Education"].fillna(df["Education"].mode()[0])
df = df.drop_duplicates()
"""
content.append(Preformatted(code2, styles["Code"]))
content.append(Spacer(1, 20))

# -------------------------------
# SECTION 3
# -------------------------------
content.append(Paragraph("3. Data Visualization", styles["Heading2"]))

content.append(Paragraph(
    "Visualization plays an important role in understanding data patterns. Various plots such as histograms and boxplots "
    "were used to analyze distributions and detect outliers.",
    styles["Normal"]
))
content.append(Spacer(1, 12))

content.append(Paragraph(
    "Histograms help in understanding how values are distributed across different ranges, while boxplots highlight "
    "variations and potential outliers in the data.",
    styles["Normal"]
))
content.append(Spacer(1, 12))

code3 = """
plt.hist(df["Age"])
sns.boxplot(x="Gender", y="SpendingScore", data=df)
"""
content.append(Preformatted(code3, styles["Code"]))
content.append(Spacer(1, 20))

# -------------------------------
# SECTION 4
# -------------------------------
content.append(Paragraph("4. Correlation Analysis", styles["Heading2"]))

content.append(Paragraph(
    "Correlation analysis helps in understanding relationships between numerical variables. "
    "A correlation matrix was generated and visualized using a heatmap.",
    styles["Normal"]
))
content.append(Spacer(1, 12))

content.append(Paragraph(
    "Values close to +1 indicate strong positive correlation, values close to -1 indicate strong negative correlation, "
    "and values near zero indicate weak or no relationship between variables.",
    styles["Normal"]
))
content.append(Spacer(1, 12))

code4 = """
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="RdBu_r")
"""
content.append(Preformatted(code4, styles["Code"]))
content.append(Spacer(1, 20))

# -------------------------------
# SECTION 5
# -------------------------------
content.append(Paragraph("5. Analysis and Insights", styles["Heading2"]))

content.append(Paragraph(
    "The analysis reveals that customer behavior varies significantly across individuals. "
    "Spending patterns are not strongly dependent on income, indicating diverse purchasing behavior.",
    styles["Normal"]
))
content.append(Spacer(1, 12))

content.append(Paragraph(
    "Most customers fall within a moderate age range, and spending scores show wide variation. "
    "These insights can help businesses understand customer segments and improve decision-making.",
    styles["Normal"]
))
content.append(Spacer(1, 12))

content.append(Paragraph(
    "Further improvements can include applying machine learning techniques such as clustering to group customers "
    "based on similar characteristics and predict future behavior.",
    styles["Normal"]
))

# -------------------------------
# BUILD PDF
# -------------------------------
doc.build(content)

print("✅ Final 2+ Page PDF Generated Successfully!")