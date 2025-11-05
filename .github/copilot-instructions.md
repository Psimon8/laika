# GitHub Copilot Instructions - AstroSuite SEO Hub

## Architecture Overview

This is a **Streamlit multi-app hub** that dynamically loads 3 independent SEO tools:

```
app.py (hub)
├─ Jsonoptimiser/json.py        → Structured Data Analyser
├─ blablamaillage-interneblabla/app.py → Internal Linking Analyzer  
└─ conversational-queries/app.py → Conversational Queries Generator
```

**Critical pattern**: Each sub-app is loaded via `importlib.util.spec_from_file_location()` and executed with `spec.loader.exec_module()`. The hub uses `st.session_state.selected_page` for navigation and `st.rerun()` to switch between apps.

## Navigation Pattern

```python
# app.py: Hub navigation
if st.button("🔍 Structured Data Analyser"):
    st.session_state.selected_page = "Structured Data Analyser"
    st.rerun()

# Then load the selected app dynamically
current_dir = os.path.dirname(os.path.abspath(__file__))
app_path = os.path.join(current_dir, 'Jsonoptimiser', 'json.py')
spec = importlib.util.spec_from_file_location("json_app", app_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)  # Executes Streamlit code
```

**Always use relative paths** with `os.path.dirname(os.path.abspath(__file__))` for cross-environment compatibility (local, Docker, cloud).

## Streamlit Conventions

### Session State Management
- **Navigation**: `st.session_state.selected_page` stores current page
- **Data persistence**: Each sub-app manages its own state keys (e.g., `gsc_data`, `zip_content`, `analysis_results`)
- **Reset pattern**: `for key in list(st.session_state.keys()): del st.session_state[key]`

### Widget Keys
**Always use unique keys** to avoid conflicts between tabs/apps:
```python
# Good: Unique keys per context
st.number_input("Concurrents", key="url_comp_count")    # Tab 1
st.number_input("Concurrents", key="manual_comp_count") # Tab 2

# Bad: Duplicate keys cause Streamlit errors
st.number_input("Concurrents")  # Same widget in 2 tabs = crash
```

### Tab Pattern (Structured Data v2.0)
```python
tab1, tab2 = st.tabs(["🔗 URLs", "📝 HTML"])
with tab1:
    # URL-based analysis
with tab2:
    # Manual HTML analysis
# Share logic via reusable functions like display_comparison_results()
```

## Sub-App Specific Patterns

### Conversational Queries (`conversational-queries/`)
**Modular architecture** with utils/ and services/:
```python
from utils.config_manager import ConfigManager
from utils.export_manager import ExportManager
from utils.workflow_manager import WorkflowManager
from services.dataforseo_service import DataForSEOService
```

**Pipeline state management**: Uses `pipeline_state` dict with signature-based invalidation to reset on config change.

### Maillage Interne (`blablamaillage-interneblabla/`)
**Performance optimization**: Uses `@st.cache_data` for expensive operations:
```python
@st.cache_data
def load_gsc_data_cached(uploaded_file, config):
    return pd.read_csv(uploaded_file)
```

**Optional dependencies**: Gracefully handles missing `pyahocorasick`, `openpyxl`, `fuzzywuzzy` with warnings.

### Structured Data Analyser (`Jsonoptimiser/`)
**HTTP fetching** for URL-based analysis:
```python
def fetch_html_from_url(url):
    headers = {'User-Agent': 'Mozilla/5.0...'}  # Avoid bot blocking
    response = requests.get(url, headers=headers, timeout=10)
    return response.text
```

## Error Handling Pattern

Every sub-app loader wraps in try/except with user-friendly messages:
```python
try:
    spec.loader.exec_module(module)
except Exception as e:
    st.error(f"❌ Erreur lors du chargement: {e}")
    st.info("Assurez-vous que toutes les dépendances sont installées.")
    with st.expander("Détails de l'erreur"):
        st.code(traceback.format_exc())
```

## Testing

Run `test_apps.py` to validate all 3 apps and dependencies:
```bash
python3 test_apps.py
```

Tests check:
- File existence
- Module structure validity
- All 11 dependencies installed (streamlit, pandas, beautifulsoup4, extruct, etc.)

**Note**: Tests don't execute Streamlit code (would fail outside runtime), only validate structure.

## Development Workflows

### Local development
```bash
streamlit run app.py          # Port 8501
./run.sh                       # Alternative launcher
```

### Adding a new feature to a sub-app
1. Edit the sub-app file directly (e.g., `Jsonoptimiser/json.py`)
2. Test in isolation: `streamlit run Jsonoptimiser/json.py`
3. Test via hub: `streamlit run app.py` → Navigate to app
4. No need to modify `app.py` unless changing navigation

### Deployment
See `DEPLOYMENT.md` for Streamlit Cloud, Docker, Heroku, AWS options. Key: Use environment variables for API keys (OpenAI, DataForSEO).

## API Keys & Configuration

**OpenAI**: Required for Conversational Queries (GPT-4o-mini question generation)
**DataForSEO**: Optional enrichment (search volumes, CPC, competition)

Config pattern in conversational-queries:
```python
config_manager = ConfigManager()
api_key, enable_dataforseo, dataforseo_config = config_manager.render_credentials_section()
```

## Documentation Structure

- `README.md`: Overview and quick start
- `GUIDE.md`: Detailed usage for each tool
- `QUICKSTART_V2.md`: Illustrated step-by-step for Structured Data v2.0
- `TROUBLESHOOTING.md`: Common issues and solutions
- `DEPLOYMENT.md`: Deployment options
- `CHANGELOG_STRUCTURED_DATA.md`: v2.0 release notes (2-tab feature)
- `VERIFICATION.md`: Manual test checklist

## Recent Major Changes

**Structured Data Analyser v2.0** (Nov 2025):
- Added 2-tab interface: URL-based analysis + manual HTML
- Refactored shared logic into `display_comparison_results()`
- Added `fetch_html_from_url()` with 10s timeout and custom User-Agent
- All documented in `CHANGELOG_STRUCTURED_DATA.md`, `PRESENTATION_V2.md`, `RECAP_V2.md`

## Key Files to Reference

- `app.py`: Hub navigation and dynamic loading pattern
- `conversational-queries/app.py`: Modular architecture example
- `Jsonoptimiser/json.py`: Tab-based UI and HTTP fetching
- `blablamaillage-interneblabla/app.py`: Caching and optional deps handling
- `test_apps.py`: Validation and dependency checking
