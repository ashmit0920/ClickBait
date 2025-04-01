# as variations is used in multiple files (like kafka_utils/consumer.py and api/routes.py, best approach is to import it from a config file)

variations = ["variation1", "variation2", "variation3"]
positive_events = ["get_started", "learn_more",
                   "sign_up", "subscribe"]  # Events with reward = 1
