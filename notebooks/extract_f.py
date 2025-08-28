import tldextract
from urllib.parse import urlparse

def extract_features(url: str) -> dict:
    parsed = urlparse(url)
    ext = tldextract.extract(url)
    
    features = {
        "url_length": len(url),
        "hostname_length": len(parsed.netloc),
        "path_length": len(parsed.path),
        "num_dots": url.count("."),
        "num_hyphens": url.count("-"),
        "num_digits": sum(c.isdigit() for c in url),
        "https": 1 if url.startswith("https") else 0,
        "subdomain_length": len(ext.subdomain),
    }
    return features
