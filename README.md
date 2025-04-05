# 📚 Books Data Dashboard – Powered by Python, DBT & Power BI

This project showcases an end-to-end data pipeline that extracts book data from the web, transforms it into analytics-ready format, and visualizes key insights using Power BI.

---

## 🚀 Project Overview

This project simulates a very basic real-world **data engineering and analytics workflow** using a public website ([Books to Scrape](http://books.toscrape.com)) as the data source. It demonstrates how to:

- 🔎 Scrape raw data from a website
- 🗃️ Load it into a PostgreSQL database
- 🧱 Transform and model it with **DBT**
- 📊 Visualize key metrics using **Power BI**

---

## 🧰 Tech Stack

| Layer        | Tool / Language                     |
|--------------|-------------------------------------|
| **Data Source** | [`books.toscrape.com`](http://books.toscrape.com) |
| **Extraction**  | Python, BeautifulSoup             |
| **Database**    | PostgreSQL                        |
| **Transformation** | DBT (Data Build Tool)             |
| **Visualization** | Power BI                        |
| **Version Control** | Git & GitHub                    |

---

## 🎯 Goals

- Practice the **ETL (Extract, Transform, Load)** process
- Use **DBT to manage SQL transformations and data models**
- Create a clean, interactive **dashboard for business insights**
- Apply software engineering practices to a data pipeline

---

## 📁 Project Structure

```bash
.
├── books_raw.csv             # Raw scraped book data
├── scrape_books.py           # Python scraper script
├── load_to_db.py             # Loads data into PostgreSQL
├── dbt_project/
│   ├── models/
│   │   ├── books_cleaned.sql # DBT transformation model
│   │   └── schema.yml        # DBT documentation configurations
├── BooksToScrape.pbix    # Final Power BI dashboard
├── README.md                 # You're here!
