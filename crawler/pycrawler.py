class Crawler:
    def __init__(self):
        pass

    def _process_url(self, url):
        pass

    def _get_links(self, url):
        pass

    def crawl(self, urls=None):
        """
        Crawls the given URLs using breadth-first search.
        
        Args:
            urls: List of URLs to crawl. If None, no crawling is performed.
        
        Returns:
            None
        """
        if not urls:
            return
            
        queue = urls.copy()  # Create a copy to avoid modifying the input
        visited = set()
        
        while queue:
            current_url = queue.pop(0)
            
            if current_url in visited:
                continue
                
            # Process the current URL
            self._process_url(current_url)
            
            # Mark as visited
            visited.add(current_url)
            
            # Get new URLs from the current URL and add them to the queue
            new_urls = self._get_links(current_url)
            for url in new_urls:
                if url not in visited:
                    queue.append(url)
        
  

        