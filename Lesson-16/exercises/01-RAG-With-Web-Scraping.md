# Using RAG for Scraping Websites in the Text Generation WebUI

1. Setup the `superbooga` extension in Text Generation Web UI
2. Select a model in the `Model` tab
   - Choose a suitable model that is trained for instruction-following tasks
3. Open the `Chat` tab
4. Select `instruct` mode
5. Ask a very specific question related to something not included in the training data
   - For example: `Calculate how many times faster is a Pagani car than a Shark`
     - An example answer would be: `I'm sorry, but I cannot provide a reply without more context. The statement "Pagani car is faster than a Shark" is not clear enough to determine the speed of both entities. Please provide more information or a specific scenario to calculate the speed of both.`
6. Scroll down to see the RAG pane
7. Select the `URL input` tab
8. Input the URL of the websites you want to scrape
   - For example use an [article about sharks](https://en.wikipedia.org/wiki/Shark) and [sport cars](https://en.wikipedia.org/wiki/Pagani_Zonda)
9. Select the `Strong cleanup` checkbox
   - This will remove short text elements like buttons, menu items, and such from the page content
10. Click on `Load data` to add the _chunks_ to the database
11. After loading the data, click on the _hamburger menu_ in the left of the input field and select `Regenerate`
12. The response should now contain information retrieved from the websites

    - An example answer would be:

    ```text
    Based on the provided information, we can calculate how many times faster a Pagani car is than a shark in terms of acceleration.
    
    The Pagani C12 can accelerate to 97 km/h (60 mph) in 4.0 seconds, and to 161 km/h (100 mph) in 9.2 seconds. This means that it can accelerate from 0 to 97 km/h in 4.0 seconds and from 0 to 161 km/h in 9.2 seconds.
    
    The average shark can swim at a speed of 8 kilometers per hour (5.0 mph) and can reach speeds upwards of 19 kilometers per hour (12 mph) when feeding or attacking.
    
    Let's assume that we want to compare the acceleration of the Pagani C12 to the acceleration of a shark. The acceleration of the Pagani C12 is 0-97 km/h in 4.0 seconds and 0-161 km/h in 9.2 seconds. The acceleration of the shark can be calculated as the difference in speed over time, which is 0-19 km/h in 1 second.
    
    Therefore, the Pagani C12 is approximately 7.5 times faster than a shark in terms of acceleration, from 0 to 97 km/h. When comparing the 0 to 161 km/h acceleration, the Pagani C12 is approximately 5.6 times faster than a shark.
    
    It's worth noting that this comparison is based on acceleration and not speed, as sharks have an average cruising speed of 5.0 mph, while the Pagani C12 has a top speed of 100 mph.
    ```
