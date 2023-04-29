from src.providers.service.browsers.browsers_library.remote_edge_browser import RemoteEdgeBrowser
from src.providers.service.browsers.browsers_library.remote_ff_browser import RemoteFFBrowser
from src.providers.service.browsers.browsers_library.remote_chrome_browser import RemoteChromeBrowser
from src.providers.service.browsers.browsers_library.chrome_browser import ChromeBrowser
from src.providers.service.browsers.browsers_library.ff_browser import FFBrowser
from src.providers.service.browsers.browsers_library.edge_browser import EdgeBrowser



class BrowsersProvider:

    BROWSER_MAPPER = {
        'chrome': ChromeBrowser,
        'ff': FFBrowser,
        'edge': EdgeBrowser,
        'remote_chrome': RemoteChromeBrowser,
        'remote_ff': RemoteFFBrowser,
        'remote_edge': RemoteEdgeBrowser
    }

    def get_driver(browser_name):
        """
        browser_name -> 'chrome, ff, edge, remote_chrome, remote_ff, remote_edge 
        """

        browser = BrowsersProvider.BROWSER_MAPPER.get(browser_name)
        if browser is None:
            raise NotImplementedError(f"Browser name {browser_name} is not supported for UI tests. Please register it in BrowsersProvider class")

        driver = browser.get_driver()
        return driver