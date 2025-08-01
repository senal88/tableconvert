# TableConvert API Scripts

This repository contains a collection of scripts that use the [TableConvert API](https://tableconvert.com/api/#overview) to convert data between various formats.

## Supported Conversions

The following conversions are supported:

- Excel to JSON
- Excel to CSV
- Excel to Markdown
- Excel to HTML
- Excel to SQL
- Excel to LaTeX
- Excel to XML
- Excel to MySQL
- Excel to MediaWiki

And the reverse conversions from each of these formats back to Excel.

## Getting Started

### Prerequisites

- Python 3.6+
- `requests` library (`pip install requests`)
- `python-dotenv` library (`pip install python-dotenv`)

### Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd tableconvert
    ```
2.  **Create a `.env` file:**
    Create a `.env` file in the root of the project and add your TableConvert API key as follows:
    ```
    TABLECONVERT_API_KEY=Xlfafl1AzdiLgqvSfyp4jc9FVBjjcPB8
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run a conversion, execute the desired script from the `scripts` directory. For example, to convert an Excel file to JSON:

```bash
python scripts/excel_to_json.py <path-to-your-excel-file>
```

