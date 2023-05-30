import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

# Sample data
total_reviews = 100
average_rating = 4.2
positive_reviews = 75
negative_reviews = 10
neutral_reviews = total_reviews - positive_reviews - negative_reviews
rating_distribution = [5, 4, 3, 2, 1]
rating_counts = [45, 30, 15, 5, 5]
positive_sentiments = 70
negative_sentiments = 20
neutral_sentiments = 100 - positive_sentiments - negative_sentiments
positive_topics = ['Topic 1', 'Topic 2', 'Topic 3']
negative_topics = ['Topic 4', 'Topic 5', 'Topic 6']
review_volume_data = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=30, freq='D'),
    'Reviews': [10, 15, 8, 12, 20, 25, 30, 28, 22, 18, 15, 12, 20, 25, 30, 28, 22, 18, 15, 12, 20, 25, 30, 28, 22, 18, 15, 12, 20, 25]
})
review_sources = ['Amazon', 'Google', 'Yelp']
review_source_counts = [60, 20, 20]
review_word_cloud = {'word1': 20, 'word2': 15, 'word3': 10, 'word4': 8, 'word5': 5}
review_feedback_counts = {'Helpful': 60, 'Unhelpful': 40}
helpful_reviews = pd.DataFrame({
    'Rating': [5, 4, 3],
    'Content': ['Review 1', 'Review 2', 'Review 3']
})
competitor_average_ratings = [4.0, 4.2, 4.1]
competitor_positive_review_percentages = [60, 65, 55]
competitor_negative_review_percentages = [10, 15, 12]
customer_age_ranges = ['18-24', '25-34', '35-44', '45-54', '55+']
customer_age_range_percentages = [10, 20, 30, 25, 15]
customer_genders = ['Male', 'Female', 'Other']
customer_gender_percentages = [40, 55, 5]
customer_locations = ['Location 1', 'Location 2', 'Location 3']
customer_location_percentages = [50, 30, 20]
response_rate = 80
average_response_time = 2.5
resolution_rate = 70

# Create Dash app
app = dash.Dash(__name__, external_stylesheets=['styles.css'])
# app = dash.Dash(__name__)

# Define layout
app.layout = html.Div(children=[ 
    
    html.H1('Review Dashboard'),

    html.Div([
        html.H3('Overview'),
        html.P(f'Total Reviews: {total_reviews}'),
        html.P(f'Average Rating: {average_rating}'),
        html.P(f'Positive Reviews: {positive_reviews}'),
        html.P(f'Negative Reviews: {negative_reviews}'),
        html.P(f'Neutral Reviews: {neutral_reviews}')
    ]),

    html.Div([
        html.H3('Rating Distribution'),
        dcc.Graph(
            figure=go.Figure(
                data=[go.Bar(x=rating_distribution, y=rating_counts)],
                layout=go.Layout(xaxis={'title': 'Rating'}, yaxis={'title': 'Count'})
            )
        )
    ]),

    html.Div([
        html.H3('Sentiment Analysis'),
        html.P(f'Positive Sentiments: {positive_sentiments}%'),
        html.P(f'Negative Sentiments: {negative_sentiments}%'),
        html.P(f'Neutral Sentiments: {neutral_sentiments}%')
    ]),

    html.Div([
        html.H3('Trending Topics'),
        html.P('Top Positive Topics: ' + ', '.join(positive_topics)),
        html.P('Top Negative Topics: ' + ', '.join(negative_topics))
    ]),

    html.Div([
        html.H3('Review Volume Over Time'),
        dcc.Graph(
            figure=go.Figure(
                data=[go.Scatter(x=review_volume_data['Date'], y=review_volume_data['Reviews'])],
                layout=go.Layout(xaxis={'title': 'Date'}, yaxis={'title': 'Reviews'})
            )
        )
    ]),

    html.Div([
        html.H3('Review Sources'),
        dcc.Graph(
            figure=go.Figure(
                data=[go.Pie(labels=review_sources, values=review_source_counts)],
                layout=go.Layout(title='Review Sources')
            )
        )
    ]),

    html.Div([
        html.H3('Review Word Cloud'),
        html.P('Word Cloud Visualization here')
    ]),

    html.Div([
        html.H3('Review Feedback'),
        html.P('Review Feedback Distribution:'),
        html.P(f'Helpful: {review_feedback_counts["Helpful"]}%'),
        html.P(f'Unhelpful: {review_feedback_counts["Unhelpful"]}%'),
        html.P('Most Helpful Reviews:'),
        html.Ul([html.Li(f'Rating: {row["Rating"]}, Content: {row["Content"]}') for _, row in helpful_reviews.iterrows()])
    ]),

    html.Div([
        html.H3('Competitor Comparison'),
        dcc.Graph(
            figure=go.Figure(
                data=[
                    go.Bar(x=competitor_average_ratings, y=competitor_positive_review_percentages, name='Positive Reviews'),
                    go.Bar(x=competitor_average_ratings, y=competitor_negative_review_percentages, name='Negative Reviews')
                ],
                layout=go.Layout(xaxis={'title': 'Average Rating'}, yaxis={'title': 'Review Percentage'}, barmode='stack')
            )
        )
    ]),

    html.Div([
        html.H3('Customer Demographics'),
        dcc.Graph(
            figure=go.Figure(
                data=[go.Pie(labels=customer_age_ranges, values=customer_age_range_percentages)],
                layout=go.Layout(title='Age Range Distribution')
            )
        ),
        dcc.Graph(
            figure=go.Figure(
                data=[go.Pie(labels=customer_genders, values=customer_gender_percentages)],
                layout=go.Layout(title='Gender Distribution')
            )
        ),
        dcc.Graph(
            figure=go.Figure(
                data=[go.Pie(labels=customer_locations, values=customer_location_percentages)],
                layout=go.Layout(title='Location Distribution')
            )
        )
    ]),

    html.Div([
        html.H3('Response and Resolution'),
        html.P(f'Response Rate: {response_rate}%'),
        html.P(f'Average Response Time: {average_response_time} days'),
        html.P(f'Resolution Rate: {resolution_rate}%')
    ]),

    html.Div([
        html.H3('Key Metrics and Goals'),
        html.P('Key metrics and goals description here')
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
