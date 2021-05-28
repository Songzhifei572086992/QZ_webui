import logging

class Logger:
    def get_log(self):
        # 创建日志器
        logger = logging.getLogger('logger')
        # 设置日志级别
        logger.setLevel(logging.DEBUG)
        if not logger.handlers:
            ftm = '%(asctime)s %(filename)s %(levelname)s %(funcName)s %(message)s'
            # 创建一个格式器
            fr = logging.Formatter(ftm)
            # 创建一个处理器 输出到文件中
            log_data = logging.FileHandler('log1.log',encoding='utf-8')
            # 创建一个处理器 输出到控制台
            sh = logging.StreamHandler()
            # 把文本加载到日志器
            logger.addHandler(log_data)
            # 把控制台加载到日志器
            logger.addHandler(sh)
            # 把格式器放入控制台
            sh.setFormatter(fr)
            # 把格式器放入到文本控制器
            log_data.setFormatter(fr)
        return logger
