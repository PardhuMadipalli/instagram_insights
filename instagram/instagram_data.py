from .restmethods import get
import constant
import re
import csv
from datetime import datetime


class Instapost:
    def __init__(self, igmedia_id, impressions, engagement, reach, timestamp, caption):
        self.id = igmedia_id
        self.impressions = impressions
        self.engagement = engagement
        self.reach = reach
        self.timestamp = timestamp
        self._caption = caption
        self.tags = self._get_hash_tags()
        self.hour = self._get_hour()

    # def print_post(self):
    #     print(self.id, end=' ')
    #     print(*self.tags, sep=' ')

    def _get_hash_tags(self):
        return [tag[1:] for tag in re.findall("[#]\w+", self._caption)]

    def _get_hour(self):
        # Sample date format is 2020-12-20T11:29:31+0000
        return datetime.strptime(self.timestamp, "%Y-%m-%dT%H:%M:%S%z").hour


def get_insights(token, page_id):
    if page_id is None or token is None:
        raise Exception("Token or page_id is none.")
    posts_response = get([page_id, 'media'], token)
    posts = []
    unique_tags = set()
    for post_dict in posts_response['data']:
        post_id = post_dict['id']
        insights_resp = get([post_id, 'insights'], token, query_params={'metric': 'impressions,engagement,reach'})
        metadata_resp = get([post_id], token, query_params={'fields': 'caption,timestamp'})
        insights_data = insights_resp['data']
        current_post = Instapost(post_id,
                                 _getvalue(insights_data[0]),
                                 _getvalue(insights_data[1]),
                                 _getvalue(insights_data[2]),
                                 metadata_resp['timestamp'],
                                 metadata_resp['caption'])
        posts.append(current_post)
        unique_tags.update(current_post.tags)
        unique_tags_list = list(unique_tags)
        headers_row = constant.DEFAULT_COLUMNS + unique_tags_list

        with open(constant.INSIGHTS_CSV, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(headers_row)
            for post in posts:
                metadata = [post.id, post.impressions, post.engagement, post.reach, post.timestamp, post.hour]
                tags_list = list(map(lambda tag: 1 if tag in post.tags else 0, unique_tags_list))
                total_row = metadata + tags_list
                csvwriter.writerow(total_row)


def _getvalue(insights_data_object):
    return insights_data_object['values'][0]['value']

