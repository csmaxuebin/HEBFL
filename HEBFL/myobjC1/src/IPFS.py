import ipfshttpclient

client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')
j = client.add('D:\oneepoch\layer2\dic4-9.txt')#提交文件至IPFS
print(j)

j = client.cat('QmdLgHBzVUJnJUtdqxU1iqxyDaMxvkevGdLTeGExg8wpy3')#从IPFS取回文件
print(j)