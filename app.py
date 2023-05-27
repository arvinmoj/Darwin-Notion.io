import os
from dotenv import load_dotenv
from notion_client import Client

#region - Import Environment Variables

load_dotenv()
NOTION_TOKEN = os.environ.get('NOTION_TOKEN')
#endregion
#region - Initialize Notion Client
notion = Client(auth="NOTION_TOKEN")
#endregion