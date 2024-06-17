
pragma solidity >=0.7.0 <0.9.0;
contract newBHZ {
    struct Node {
        //uint ID; //结点的区块链地址
        uint layer;//节点属于的异步层
        uint lazy;//懒惰次数
        bool valid;//是否是有效节点
        bool isVerifier;//是否是验证者
    }
    //string PUBLIC_KEY = 'QmXMvGeDd5EBCWSD9XxiiVsrKgrfvTkGA6aUuqRiBpZeSi';
    //暂分为三层
    string[3]  layerIpfs1 = ['0','0','0'];
    string[3]  layerIpfs2 = ['0','0','0'];
    string[3]  layerIpfs3 = ['0','0','0'];

    
    //每层应有节点数几个
    uint[3]  layerNum = [0,0,0];
    uint[3]  FedNum = [0,0,0];
    //每层模型版本,每层聚合好的模型
    uint[3]  layerVersion =[0,0,0];
    string[3]  subfedavg = ['0','0','0'];
    mapping(uint => Node) public addrMatch;//节点与其地址对应表

    function Regist(uint _id,uint _layer,bool _isVerifier) public {
//节点一开始要注册的函数
        addrMatch[_id].layer = _layer;
        addrMatch[_id].isVerifier = _isVerifier;
        addrMatch[_id].lazy = 0;    
        addrMatch[_id].valid = true;
        if(_layer==1)
        {
            layerNum[0]++;
        }else if(_layer==2){
            layerNum[1]++;
        }else if(_layer==3){
            layerNum[2]++;
        }
    }

    function addLazy(uint _id) public {//提交懒惰结果后要调用的函数
        addrMatch[_id].lazy += 1;
           if(addrMatch[_id].lazy >= 3)//提交懒惰结果的次数判别
        {
           addrMatch[_id].valid = false;//如果等于三次，那么就让这个节点无效
           layerNum[addrMatch[_id].layer - 1] = layerNum[addrMatch[_id].layer - 1] -1;
        }
      
    }

    function toxTermin(uint _id) public {//中毒节点判别函数

        addrMatch[_id].valid = false;//如果有一次中毒提交，那么直接将节点置为无效
        layerNum[addrMatch[_id].layer - 1] = layerNum[addrMatch[_id].layer - 1] -1;

    }

    function subIsfull() public  returns(uint){//判别是不是有层全提交完了

        if(layerIpfs1.length == layerNum[0])
        {   
            return 1;
        }else if(layerIpfs2.length == layerNum[1])
        {
            if(layerVersion[0] - layerVersion[1] > 4)
            {
                subfedavg[1] = subfedavg[0];
                FedNum[1] = 1;
                return 20;
            }else
            {
                return 2;
            }
        
        }else if(layerIpfs3.length == layerNum[2])
        {
            if(layerVersion[0] - layerVersion[2] > 4)
            {
                subfedavg[2] = subfedavg[0];
                FedNum[2] = 1;
                return 30;
            }else
            {
                return 3;
            }
        }
        else//没有层全提交完，还得等待
        {
            return 0;
        }

    }

    function OverSubmit(uint _id, string memory _IPFS) public {

        //训练节点训练完后，上传模型放入IPFS然后返回的哈希地址string存进数组
        if(addrMatch[_id].valid == true)
        {
            if(addrMatch[_id].layer==1)
            {
                layerIpfs1[_id - 1] = _IPFS;

                
            }else if(addrMatch[_id].layer==2){
                layerIpfs2[_id - 4] = _IPFS;

                
            }else if(addrMatch[_id].layer==3){
                layerIpfs3[_id - 7] = _IPFS;
            }
        }
        }       
    
    //把塞满的一层结果取回验证者那里
        function fetchGroup(uint _layer) public  returns(string[3] memory){
            if(_layer==1)
        {     
            
            return (layerIpfs1);
                       
        }else if(_layer==2){       
            return (layerIpfs2);
            
            
        }else if(_layer==3){
            return (layerIpfs3);    
        }   
        
        }

//训练节点取回全局模型
     function fetchFedAvg(uint _id) public returns(string memory){
                if(addrMatch[_id].layer==1)
            {   
                if(FedNum[0] == 1){
                    FedNum[0] = 0;
                    //delete layerIpfs1;
                    return (subfedavg[0]);
                }                        
            }else if(addrMatch[_id].layer==2){     
                if(FedNum[1] == 1){
                    FedNum[1] = 0;
                    //delete layerIpfs2;
                    return (subfedavg[1]);
                }       
            }else if(addrMatch[_id].layer==3){
                if(FedNum[2] == 1){
                    FedNum[2] = 0;
                    //delete layerIpfs3;
                    return (subfedavg[2]);
                }            
            }
        }          
//验证者将聚合后结果提交上来
       function subFedavg(string memory _IPFS,uint _layer) public {
            if(_layer==1)
            {   
                subfedavg[0] = _IPFS;
                layerVersion[0]++;
                delete layerIpfs1;
                FedNum[0] = 1;
            }else if(_layer==2){       
                subfedavg[1] = _IPFS;
                layerVersion[1]++;
                delete layerIpfs2;
                FedNum[1] = 1;
            }else if(_layer==3){
                subfedavg[2] = _IPFS;
                layerVersion[2]++;
                delete layerIpfs3;
                FedNum[2] = 1;
            }      
    }

        function ViewLayerIPFS() public view returns(string[3] memory,string[3] memory,string[3] memory,string[3] memory,uint[3] memory,uint[3] memory,uint[3] memory){
        return (layerIpfs1,layerIpfs2,layerIpfs3,subfedavg,layerNum,layerVersion,FedNum);
    }

        function ViewNode(uint _id) public view returns(Node memory){
        return addrMatch[_id];
    }

        function ViewFed(uint _layer) public view returns(uint){

        return FedNum[_layer - 1];
    }
    // function StrCmp(string memory _IPFS)public{
    //         bytes memory _s1=bytes(_IPFS);
    //         bytes memory _s2=bytes(s2);
    //         uint len=_s1.length;
    //         for(uint i=0;i<len;i++){
    //             if(_s1[i]!=_s2[i])
    //                 return false;
    //         }
    //         return true;
    //     }

}