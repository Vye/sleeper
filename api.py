import os
import asyncio

import responder


api = responder.API()
in_progress_count = 0


@api.route("/sleep/{seconds}")
async def greet_world(req, resp, *, seconds):
    global in_progress_count

    in_progress_count += 1
    await asyncio.sleep(float(seconds))
    in_progress_count -= 1

    resp.html = f'<html><body>{seconds} seconds later... *yawn* I\'m awake... I\'m awake...<br>'

    version = os.getenv('VERSION')
    if version:
        resp.html += f'Version: {version}<br>'

    resp.html += f'In Progress: {in_progress_count}<br>'

    resp.html += '</body></html>'


if __name__ == '__main__':
    api.run()
