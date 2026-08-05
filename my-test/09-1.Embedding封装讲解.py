{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b1eca4c6-f03f-4402-bcec-45bee79b6695",
   "metadata": {},
   "outputs": [],
   "source": [
    "from typing import List\n",
    "from langchain_core.embeddings import Embeddings\n",
    "\n",
    "class ZhipuAIEmbeddings(Embeddings):\n",
    "    \"\"\"`Zhipuai Embeddings` embedding models.\"\"\"\n",
    "    def __init__(self):\n",
    "        \"\"\"\n",
    "        实例化ZhipuAI为values[\"client\"]\n",
    "\n",
    "        Args:\n",
    "\n",
    "            values (Dict): 包含配置信息的字典，必须包含 client 的字段.\n",
    "        Returns:\n",
    "\n",
    "            values (Dict): 包含配置信息的字典。如果环境中有zhipuai库，则将返回实例化的ZhipuAI类；否则将报错 'ModuleNotFoundError: No module named 'zhipuai''.\n",
    "        \"\"\"\n",
    "        from zhipuai import ZhipuAI\n",
    "        self.client = ZhipuAI()\n",
    "\n",
    "class ZhipuAIEmbeddings(Embeddings):\n",
    "    \"\"\"`Zhipuai Embeddings` embedding models.\"\"\"\n",
    "    def __init__(self):\n",
    "        \"\"\"\n",
    "        实例化ZhipuAI为values[\"client\"]\n",
    "\n",
    "        Args:\n",
    "\n",
    "            values (Dict): 包含配置信息的字典，必须包含 client 的字段.\n",
    "        Returns:\n",
    "\n",
    "            values (Dict): 包含配置信息的字典。如果环境中有zhipuai库，则将返回实例化的ZhipuAI类；否则将报错 'ModuleNotFoundError: No module named 'zhipuai''.\n",
    "        \"\"\"\n",
    "        from zhipuai import ZhipuAI\n",
    "        self.client = ZhipuAI()\n",
    "        \n",
    "def embed_query(self, text: str) -> List[float]:\n",
    "        \"\"\"\n",
    "        生成输入文本的 embedding.\n",
    "\n",
    "        Args:\n",
    "            texts (str): 要生成 embedding 的文本.\n",
    "\n",
    "        Return:\n",
    "            embeddings (List[float]): 输入文本的 embedding，一个浮点数值列表.\n",
    "        \"\"\"\n",
    "\n",
    "        return self.embed_documents([text])[0]  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b4f3278d-11f9-426e-9765-c9c8c4694c93",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.10",
   "language": "python",
   "name": "python310"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
