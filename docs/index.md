# Example API

This application is responsible for serving an API which greets people.

It's developed using [FastAPI](https://fastapi.tiangolo.com/), because by doing so I got
OpenAPI compliant documentation being spat out with no additional effort, and that's
always fun.

I then went a bit overboard, so its got (very) basic authentication, and advertises a
bunch of servers that you can connect to it via. This is quite fun, because it means
that it all happily works within Backstage's API browser.
