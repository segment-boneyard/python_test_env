from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from flask import Flask
import analytics

analytics.write_key = "QYWnV1V9D6Rstfchrd9uSpJwFOlE0X54"

app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/")
def index():

    analytics.track('33333', 'Completed Order 2',
                    {'orderId': '23452',
                     'revenue': 29.95,
                     'currency': 'USD'
                     })
    return "SENT event   "


if __name__ == "__main__":
    app.run(debug=True)
