# -*- coding: utf-8 -*-
from logging import getLogger, config, StreamHandler, DEBUG
import os

import sys
from logutil import LogUtil
from importenv import ImportEnvKeyEnum
import importenv as setting

import boto3

PYTHON_APP_HOME = os.getenv('PYTHON_APP_HOME')
logger = getLogger(__name__)
log_conf = LogUtil.get_log_conf(PYTHON_APP_HOME + '/config/log_config.json')
config.dictConfig(log_conf)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

if __name__ == '__main__':
  codecommit_clinent = boto3.client('codecommit',
    aws_access_key_id = setting.ENV_DIC[ImportEnvKeyEnum.AWS_ACCESS_KEY_ID.value],
    aws_secret_access_key = setting.ENV_DIC[ImportEnvKeyEnum.AWS_SECRET_ACCESS_KEY.value],
    region_name = setting.ENV_DIC[ImportEnvKeyEnum.REGION_NAME.value]
  )
  
  response = codecommit_clinent.get_merge_conflicts(
    repositoryName = setting.ENV_DIC[ImportEnvKeyEnum.REPOSITORY_NAME.value],
    sourceCommitSpecifier = setting.ENV_DIC[ImportEnvKeyEnum.FROM.value],
    destinationCommitSpecifier = setting.ENV_DIC[ImportEnvKeyEnum.TO.value],
    mergeOption = 'FAST_FORWARD_MERGE'
  )
  
  if response['mergeable']:
    logger.info('マージできる')
  else:
    logger.info('マージできない')