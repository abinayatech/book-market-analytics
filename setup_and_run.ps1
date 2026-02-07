Write-Host "Step 1: Installing dependencies..."
pip install -r requirements.txt
if ($LASTEXITCODE -ne 0) { 
    Write-Error "Failed to install dependencies."
    exit $LASTEXITCODE 
}

Write-Host "Step 2: Running scraper to generate dataset..."
Set-Location scraper
scrapy crawl books
if ($LASTEXITCODE -ne 0) { 
    Write-Error "Failed to run scraper."
    exit $LASTEXITCODE 
}

Write-Host "Success! books.db has been generated in the project root."
Write-Host "You can now run the dashboard with: streamlit run dashboard/app.py"
