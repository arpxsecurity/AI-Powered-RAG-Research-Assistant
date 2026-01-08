import arxiv
import ssl
import os
from config import DOWNLOAD_DIR

# Ignore SSL certificate errors like "CERTIFICATE_VERIFY_FAILED"
ssl._create_default_https_context = ssl._create_unverified_context

def search_and_download(query, max_results=2):
    client = arxiv.Client()
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    results = list(client.results(search))
    if not results:
        return [], "No papers found."

    papers_data = []
    logs = []

    for result in results:
        paper_id = result.entry_id.split('/')[-1]
        file_name = f"{paper_id}.pdf"
        file_path = os.path.join(DOWNLOAD_DIR, file_name)

        # Download if missing
        if not os.path.exists(file_path):
            result.download_pdf(dirpath=DOWNLOAD_DIR, filename=file_name)
            logs.append(f"Downloaded: {result.title}")
        else:
            logs.append(f"Already exists: {result.title}")
        
        # Collect Metadata for the Database
        papers_data.append({
            "path": file_path,
            "title": result.title,
            "authors": ", ".join([a.name for a in result.authors]),
            "published": result.published.strftime("%Y-%m-%d"),
            "url": result.entry_id,
            "id": paper_id
        })

    return papers_data, "\n".join(logs)