from behave import given

from requestObejects.postcodes import PostCodes

postCodes = PostCodes()


@given(u'User searches for postal codes with text "{lookupText}"')
def step_impl(context, lookupText):

    result = postCodes.getPostcodeSuggestions(lookupText)
    context.SearchResults = result


@given(u'User must get list of matching valid post codes')
def step_impl(context):

    for code in context.SearchResults:
        postCodes.getPostcodeDetails(code)
