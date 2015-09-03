# django-multi-forms
Method for multiple forms in one view on one page

## Notes
This is not a Django app for use within a project. It's a simple example of how to accomplish using multiple forms in one view on one page. You should be able to copy the code into your project and make it work with minimal effort, provided you are already using class-based views.

If you need assistance, I'd be happy to help. Contact me through www.pdxpixel.com

## Usage

This method assumes you have an app such as comments. In my case, I had an app called board and within the board, there were cards, each of which could have multiple comments... The user can add comments, similar to how how you can comment to any tweet. The model would contain a comment class that would have a field message. The form would have a `ModelForm` class to add the comment.

Then, to get multiple forms, in the template, you would loop through (in my case, cards in a board) whatever model you are using and each one would have a comment form. So if there were multiple cards with multiple comments (as in my case), each would have a form. What makes this method cool is that I have an add card form on the same page, as well. So this can coexist with the many comment forms.

Remember, this is not a reusable app, just an example with code snippets. I am working on making it into an app for use in complete projects.
