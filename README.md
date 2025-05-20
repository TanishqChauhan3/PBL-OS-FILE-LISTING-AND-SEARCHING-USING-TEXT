# FILE LISTING AND SEARCHING USING TEXT

📝 Table of Contents
Overview

Features

Installation

Usage

Technical Details

File Processing

Error Handling

UI Components

---------------------------------------------------------------------------------------

🌟 Overview
This is a powerful desktop application built with Python and PyQt6 that provides two main functionalities:

File Search: Search for text patterns across multiple file types (TXT, DOCX, XLSX, PDF)

CSV Merger: Combine multiple CSV files into one with header validation

The application features a modern dark theme UI with progress tracking and comprehensive error handling.

-----------------------------------------------------------------------------------------------------------
✨ Features
🔍 File Search Capabilities
Search across multiple file formats:

Text files (.txt)

Word documents (.docx)

Excel spreadsheets (.xlsx)

PDF documents (.pdf)

Advanced search options:

Case sensitive matching

Whole word matching

Regular expression support

File expiration system (automatically moves files after specified time)

Results display with match locations and counts

Export search results to CSV

-----------------------------------------------------------------------------------------------
📊 CSV Merger
Combine multiple CSV files

Header validation to ensure consistency

Option to include/exclude headers in output

Progress tracking during merge operations
----------------------------------------------------------------------------

🖥️ General Features
Modern dark theme UI

Responsive design with progress indicators

Comprehensive error logging

Multi-threaded operations to prevent UI freezing
------------------------------------------------------------------------------------------------

💻 Installation
Prerequisites
Python 3.8+

pip package manager

Installation Steps
Clone the repository:

bash
git clone https://github.com/yourusername/file-search-csv-merger.git  
cd file-search-csv-merger  
Create and activate a virtual environment (recommended):

bash
python -m venv venv  
source venv/bin/activate  # On Windows use: venv\Scripts\activate  
Install required dependencies:

bash
pip install -r requirements.txt  
🚀 Usage
Running the Application
bash
python main.py  
------------------------------------------------------------------------------------------
🔍 File Search
Select input location (file or folder)

Enter search text

Configure search options (case sensitivity, whole word, regex)

(Optional) Set output folder for matching files

(Optional) Configure file expiration settings

Click "Start Search"
-----------------------------------------------------------------------------------------------------

📊 CSV Merger
Select multiple CSV files to merge

Choose output file location

Configure merge options (include headers)

Click "Merge CSV Files"
------------------------------------------------------------------------------------------
🔧 Technical Details
Architecture
The application follows a Model-View-Controller (MVC) pattern with:

Model: SearchThread and CSVThread classes handle core functionality

View: PyQt6-based UI components

Controller: FileSearchApp class manages interactions

Multi-threading
Search and merge operations run in separate QThreads

Prevents UI freezing during long operations

Progress updates communicated via signals
-----------------------------------------------------------------------------------------------
🛠️ File Processing
Each file type is handled differently:

File Type	Library Used	Processing Method
.txt	Built-in	Line-by-line reading
.docx	python-docx	Paragraph processing
.xlsx	openpyxl	Cell-by-cell reading
.pdf	PyPDF2	Page text extraction
---------------------------------------------------------------------------------------------------
⚠️ Error Handling
Comprehensive Logging
All errors logged to file_search_errors.log

Log format: [timestamp] [level] [message]

Includes context about failed operations

User Feedback
Friendly error messages in UI

Detailed tooltips and status updates

Modal dialogs for critical errors

Graceful Recovery
Thread-safe operation stopping

Resource cleanup on exit

Partial result preservation
-----------------------------------------------------------------------------------------------
🖥️ UI Components
Main Window
Tabbed interface (Search/CSV Merge)

Responsive layout with scroll areas

Dark theme with consistent styling

Search Tab
Input location selection

Search options panel

Output configuration

Results table with sorting

CSV Merge Tab
File selection controls

Merge options

Progress indicators
