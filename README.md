<h2>Mud & Cogs</h2>

Mud & Cogs is an ecom website where an user can view and purchase mountain bike parts for their mountain bike.
The user can browse three different parts of the mountain bike, they are: Drivetrain components( gears), Brakes and
Tyres. When the user has found the part they are looking for, they can add the part to the basket. Once they have
complete their shopping, they can click on the basket and view all the parts they have added to the basket. If they
happy with their shopping they can complete their order by clicking on the complete order link and complete the form
with their details and card details. When that is completed they will taking to a page saying the payment has been 
successful and give their order number.

Please <a href="">Click Here</a> to see the database schema.

<hr/> 

<h3>UX</h3>

<strong>Categories</strong> - The user can use the category links on the navbar to move between the all the parts or one of the other categories:
                              Drivetrain, Brakes, Tyres. Under each of these categories the user will see only the parts of that aparticular category.

<strong>Search Bar</strong> - The user can click on the Search bar to search for any of the items on the website, by typing in keywords. for example 
                              Brakes, Tyres or chain and then click on the search button. All the items with that keyword will appear on the page below
                              for the user to look at and choose whether they want to add any of those items to their basket and how many of the item they want.
                                                
<strong>Add or Remove Quantity</strong> - When the user is looking at an item, they can add more and remove the amount of the item they want to purchase.
                                          Once they have the choosen the correct they want and can click on the add to basket button to add the amount of
                                          items they want to purchase. Once they have clicked on the add to basket button the amount will appear under the
                                          basket and the item/s will appear in the basket.

<strong>Basket</strong> - In the basket the user will find all the item/s they have added to the basket will they were shopping. From the user can either add
                          more items by changing the quantity of the items or click on the keep shopping button to add any other item/s to the basket.
                          Once they are finished shopping the user can click on the secure payment button and they will be taken to a payment page.

<strong>Secure Payment</strong> - When the user is ready to do the payment for all the items they want and clicked on the Secure Payment button.
                                  the user will be taken to a page where they will have to fill in a form with all their details, to where the parcel
                                  needs to be send. At the end of the page the user will need to fill in their card details to make a secure payment.
                                  If any of their details are incorrect the form or card will show the error where the error is or in red. 

<hr/> 

<h3>Design</h3>

I have used the a program called Figma that helped design the pages and this makes them easy to use and keeps them uncluttered.
The user can see and read everything clearly without having to do an indepth search for what the are looking for. The approach to the design was to make
the website easy to navigate and inviting so anyone can use this with ease.

Please <a href="">Click Here</a> to see the design.

<hr/> 

<h3>Features</h3>

<ul>
    <li>Navbar with categories, when clicked should take you to the category you clicked on.</li>
    <li>Search bar where keywords are used to find items in the database.</li>
    <li>Add to basket link, where you can add items to your basket.</li>
    <li>Keep shopping button, that will return you to the home page.</li>
    <li>Secure payment, which will take the user to a form that needs to be filled in.</li>
</ul>    

<hr/> 

<h3>Technology</h3>

<h4>Langauges</h4>
    <ul>
        <li><a href="https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5">HTML5</a>: was used for the rendering of the template design.</li>
        <li><a href="https://www.w3schools.com/css/">CSS3</a>: was used for the rendering of the template style.</li>
        <li><a href="https://www.python.org/">Python</a>: was used for the rendering of the application logic.</li>
    </ul>
<h4>Database</h4>
    <ul>
        <li><a href="https://docs.python.org/3/library/sqlite3.html">Sqlite3</a>: was used for the database.</li>
        <li><a href="https://aws.amazon.com/console/">AWS</a>: was used for the storaged of the images.</li>
    </ul>   
<h4>Frameworks</h4>
    <ul>
        <li><a href="https://www.djangoproject.com/">Django</a>: was used for creating routes and the rendering of the HTML5 templates.</li>
        <li><a href="https://getbootstrap.com/">Bootstrap</a>: was used for the navigation and responsiveness.</li>
    </ul>
<h4>Tools</h4>
    <ul>
        <li><a href="https://git-scm.com/">GitHub/Gitpod</a>: was used for writing up all the code.</li>
        <li><a href="https://www.figma.com/">Figma</a>: was used for the design layout of the website.</li>
        <li><a href="https://www.heroku.com/">Heroku</a>: was used for the deployment of the website.</li>
    </ul>

<hr/>

<h3>Testing<h3>

<h4>Validation of Code</h4>

With the validation of the code using the following two validation sites. Using W3C validation all the HTML that was written was correct, but all the Django
inputs come up with errors. As this is not part the HTML5 language. Using the W3C CSS validation for the CSS3 that was written, the result was No Errors Found.

<h4>Manual Testing</h4>
<ol>
    <li>
        <h5>Responsive</h5>
        <ul>
            <li>
            Used Chrome dev tools and to test the responsiveness of the wed site. When resizing the screen from 4k screen, laptop, tablet and iphone
            and is responding correctly. Did test if the website will work on other browsers and loaded up correctly.
            </li>    
        </ul>
    </li>
    <li>
        <h5>Mud & Cogs link</h5>
            <ul>
                <li>
                Mud & Cogs link, when you click on any of the links and go off the home page. 
                Click on the Mud & Cogs and that will redirect back to the home page.
                </li>  
            </ul>
    </li>
    <li>
        <h5>Navbar links</h5>
            <ul>
                <li>
                Clicked on the all parts link.
                Will open a new page with all the parts displaying in their own box.
                Each box will display an item image, item name and item price.
                </li>    
            </ul>
    </li>
    <li>
        <h5>Part links</h5>
            <ul>
                <li>
                Clicked on one part and a new page opens with the part details.
                Where I can update the amount of the part I am going to buy.
                Clicked on the 'Keep shopping' button, which will take me back to the home page.
                Clicked on the 'Add to basket' button, which will take me to the basket page.
                </li>    
            </ul>
    </li>
    <li>
        <h5>Basket page</h5>
            <ul>
                <li>
                Clicked on the basket link.
                Will redirect to the basket page, where I can see all the parts I want to buy.
                Or if there is no parts in the basket, it will display ' Your basket is empty'.
                Clicked on the 'Keep shopping' link and redirected back to the home page and I can keep on shopping.
                Or clicked on the 'Secure payment' button and redirect to the payment page.
                </li>    
            </ul>
    </li>
    <li>
        <h5>Delete Recipe</h5>
            <ul>
                <li>
                Clicked on the Delete recipe button,
                The recipe is deleted form the database,
                The Delete recipe page will redirect you to the display recipe page,
                A message will appear stating the recipe has been deleted.
                </li>    
            </ul>
    </li>
    <li>
        <h5>Sign Out</h5>
            <ul>
                <li>
                Clicked on the Sign out link,
                The Sign Out will redirect you to the Home page,
                A message will appear stating You have been Signed Out! Good Bye.
                </li>    
            </ul>
    </li> 
</ol>

<hr/>

<h4>Deployment</h4>

I used the Heroku app to deploy my application and I deployed in the following way:
<ol>
    <li>I created my app under my-yummy-dishes</li>
    <li>Create a Heroku remote</li>
    <li>Create a Profile and requirements file</li>
    <li>Pushed my new project to Heroku</li>
    <li>Create a web process using heroku ps:scale web=1 in the terminal</li>
    <li>Set my config vars IP 0.0.0.0 and the PORT 8080</li>
    <li>Set my MONGO_URI in config vars</li>
    <li>Refershed my dyno's</li>
    <li>Opened my app the see if the app is working correctly</li>
</ol>    

<hr/>

<h4>Acknowledgements</h4>

The recipes I used was from the BBC recipe website and everyone on the Slack that gave me so much advise. 
YOUTUBE - PrettyPrint for all his video's how to work with flask, python and MongoDB. 