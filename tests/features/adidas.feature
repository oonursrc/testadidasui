Feature: Automate adidas webpage

    Scenario Outline: Web page is running
        Given Adidas web page is running on <browser>
        Then webpage title is <title>
        Examples:
            | browser   | title                       |
            | chrome    | adidas Official Website UK  |


    Scenario Outline: Search for a product
        When <key> word is searched
        Then new url is <url>
        Examples:
            | key      | url                                        |
            | running  | https://www.adidas.co.uk/search?q=running  |


    Scenario Outline: Add a product to the cart
        When click on the first product
        And select a size
        And add to bag
        Then new url is <url>
        And there are <count> product in the cart
        Examples:
            | url                                                           |count |
            | https://www.adidas.co.uk/adizero-boston-10-shoes/H67513.html  |1     |
