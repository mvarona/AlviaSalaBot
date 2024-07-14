## Code
`tweet.py` is tested using [`Unittest`](https://docs.python.org/3/library/unittest.html) on `test_tweet.py`. The third-party libraries [`requests`](https://pypi.org/project/requests/), [`requests_oauthlib`](https://pypi.org/project/requests-oauthlib/) and [`python-dotenv`](https://pypi.org/project/python-dotenv/) are used for network access, OAuth authentication, and secrets handling, respectively.

## Infrastructure
The tweetbot code can be run in a [Google Cloud function](https://cloud.google.com/functions), with the following considerations:

- The secrets must be managed directly at the Google Cloud function, so the `python-dotenv` import has to be removed.
- The Google Cloud function entrypoint (`make_request()`) takes the following parameters: `(*args, **kwargs)`, and cannot return a boolean value. Returning a string is enough for this purpose.
- As the Google Cloud function has its own entrypoint, the `main()` function can be removed, as well as its conditional invocation at the end of the file.

In order to work, a Twitter account and [API keys](https://developer.x.com/en/docs/authentication/oauth-1-0a/api-key-and-secret) are needed. They can be managed from the [Twitter Developer portal](https://developer.twitter.com/en/portal/dashboard).

To periodically run the function, an HTTP trigger can be created and invoked from [Google Cloud Scheduler](https://cloud.google.com/scheduler).
