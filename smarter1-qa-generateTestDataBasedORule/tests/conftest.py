# conftest.py
def pytest_html_results_summary(prefix, summary, postfix):
    # You can modify prefix, summary, or postfix lists to add your HTML content
    summary.extend([f"<p>Custom summary info here</p>"])
