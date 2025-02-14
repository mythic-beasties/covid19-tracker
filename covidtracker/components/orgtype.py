import dash_core_components as dcc
import dash_html_components as html

from ..settings import THREESIXTY_COLOURS
from ._utils import horizontal_bar


def orgtype(grants):
    orgtypes = [
        {"name": i, "count": count}
        for i, count in grants["_recipient_type"].value_counts().iteritems()
    ]
    count_unknown = grants["_recipient_type"].isnull().sum()
    if count_unknown:
        orgtypes.append({"name": "Unknown", "count": count_unknown})

    return html.Div(
        className="base-card base-card--red grid__1",
        children=[
            html.Div(
                className="base-card__content",
                children=[
                    html.Header(
                        className="base-card__header",
                        children=[
                            html.H3(
                                className="base-card__heading",
                                children="Type of recipients",
                            ),
                            html.H4(
                                className="base-card__subheading",
                                children="Number of grants",
                            ),
                        ],
                    ),
                    dcc.Graph(
                        id="orgtype-chart-chart",
                        figure=horizontal_bar(
                            orgtypes,
                            colour=THREESIXTY_COLOURS[3],
                        ),
                        config={"displayModeBar": False, "scrollZoom": False},
                    ),
                ],
            ),
        ],
    )
