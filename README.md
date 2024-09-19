# kilter-board

The Kilterboard is a standardized training tool for climbers. It is a wall with an adjustable angle and screwed on holds with LEDs which allows users to create their own climb and comes in various sizes.

Climbs come with various levels of difficulties (grades). These are initially set by the creater of the climb (setter) and users who complete the climb can also submit their own grades to help come to a concensus.

We shall use the data from the Kilterboard in order to develop a model that can accurately grade climbs. Although the Kilterboard boosts a large repository of climbs (almost 200,000), most users only attempt the most popular climbs which can have up to 40,000+ ascents while a large portion of climbs have less than 5 ascents.

This hurts the user experience since some setters do not grade their climbs accurately due to inexperience or lack of climbing ability/knowledge. However if these climbs remain unpopular, it is unlikely if a wrong grade will be changed as there will not be enough user-submitted ratings to correct the error.

This model will not only allow setters to set and grade climbs more accurately but will also give the larger userbase access to more climbs in their desired difficulty range outside of the most popular climbs which users rely on due to their accurate grades.

Data for this project can be found at:
https://climbdex.fly.dev/

https://github.com/lemeryfertitta/Climbdex

Climbs on the Kilterboard look like the following:


![6a-V3-1](https://github.com/user-attachments/assets/d59f36a4-6b29-415a-ab6e-a123644bbbea)
![7b-V8-1](https://github.com/user-attachments/assets/f948981f-6f7f-4b54-870a-4787217ce46f)

Note that various holds in each image are circled which represent which holds are allowed / make up a particular climb. These holds are further differentiated by color: green represents the starting holds, yellow represents a foothold, blue represents a handhold and purple represents the finishing hold. A climb begins at the starting hold and ends at the finishing hold(s). A foothold can only be used by a foot while a handhold can be used by both a hand and foot.

We tackle this problem in a few different ways. First we work with the tabular data given by the boardlib database. This allows us to incorporate more features such as the angle of the climb as well as potentially useful information found in user-submitted descriptions of each climb (some climbs have specific instructions such as campus which means you cannot use your feet). We will treat this problem as an ordinal regression problem. We will utilize classical machine learning methods such as Random Forest, linear regression and XGBoost.

We also work with image data by scraping images from the climbdex.fly.dev website. Using image data, we can potentially identify more complex information such as the distance between various holds. However we also lose some information compared to using tabular data since we are no longer able to incorporate important data such as the angle of the climb. In this case, we will approach the problem as an image classification problem. We will use deep learning methods such as a Convolutional Neural Network and transfer learning.
