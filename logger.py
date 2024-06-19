import tensorflow as tf

class Logger:
    """
    tensorboard logger
    """

    def __init__(self, log_dir):
        """
        initialize summary writer
        """
        self.writer = tf.summary.create_file_writer(log_dir)

    def scalar_summary(self, tag, value, step):
        """
        add scalar summary
        """
        with self.writer.as_default():
            tf.summary.scalar(name=tag, data=value, step=step)
            self.writer.flush()
