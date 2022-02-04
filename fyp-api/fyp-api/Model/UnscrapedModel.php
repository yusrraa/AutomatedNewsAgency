<?php
require_once PROJECT_ROOT_PATH . "/Model/Database.php";

class UnscrapedModel extends Database
{
    public function getUnscraped()
    {
        return $this->select("SELECT usd.unprocessed_news_topic, 
                            usd.unprocessed_news_description, usd.publication_date, 
                            usd.image_href FROM unprocesssed_scrape_data as usd 
                            ORDER BY id ASC");
    }
}