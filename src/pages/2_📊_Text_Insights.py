from main import get_all_rekt_summaries, get_graphql_client
from bertopic import BERTopic

gql_client = get_graphql_client()

df = df = get_all_rekt_summaries(client=gql_client, limit=175)
docs = df.to_list()

topic_model = BERTopic(verbose=True, n_gram_range=(1, 3), min_topic_size=5)
topics, probs = topic_model.fit_transform(docs)

fig = topic_model.visualize_topics()
fig.show()
