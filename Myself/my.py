import json,ast
import agent
import pandas as pd
import numpy as np
import time

def thread():
    print("Starting thread")
    agent_ = agent.Agent()
    epsilon = 0.2
    step = 0
    reward_list = []
    while True:
        print("----------------- step %d -----------------" % step)
        step += 1
        state = get_state()
        action,q_value = agent_.get_action([state],epsilon)
        print("action:  ",action)

        file = './Routing/1_2.json'
        paths = []
        with open(file,'r') as json_file:
            paths = json.load(json_file)
        print(paths['1']['2'][action])

        drl_paths = get_dRL_paths()
        drl_paths['1']['2'] = paths['1']['2'][action]

        
        
        with open('./drl_paths.json','w') as json_file:
            json.dump(drl_paths, json_file, indent=2)
        reward = path_metrics_to_reward()
        time.sleep(10)
        next_state = get_state()
        reward_ = reward['1']['2'][action]
        agent_.append_sample(state,action,next_state,reward_)
        print(reward_)
        reward_list.append(reward_)
        
        print(reward_list)

        if len(agent_.memory) > agent_.batch_size:
                agent_.update()
                if step % 20 == 0:
                    agent_.update_target()
        
        


def get_state(): # get the current network state
    file = "./net_info.csv"
    data = pd.read_csv(file)
    state = np.zeros((37,3))
    for i in range(37):
            state[i][0] = data["bwd"][i]
            state[i][1] = data["delay"][i]
            state[i][2] = data["pkloss"][i]
    return state

def get_dRL_paths():

    file = './drl_paths.json'
    with open(file,'r') as json_file:
        paths_dict = json.load(json_file)
        paths_dict = ast.literal_eval(json.dumps(paths_dict))
        return paths_dict      

def path_metrics_to_reward():
        
    file = './paths_metrics.json'
    rewards_dic = {}
    metrics = ['bwd_paths','delay_paths','loss_paths']

    try:
        with open(file,'r') as json_file:
            paths_metrics_dict = json.load(json_file)
            paths_metrics_dict = ast.literal_eval(json.dumps(paths_metrics_dict))
    except:
        time.sleep(0.35)
        with open(file,'r') as json_file:
            paths_metrics_dict = json.load(json_file)
            paths_metrics_dict = ast.literal_eval(json.dumps(paths_metrics_dict))
    for i in paths_metrics_dict:
        rewards_dic.setdefault(i,{})
        for j in paths_metrics_dict[i]:
            rewards_dic.setdefault(j,{})
            for m in metrics:
                if m == metrics[0]:
                    bwd_cost = [] #since the DRL will minimize reward function, we do 1/bwd for such function
                    for val in paths_metrics_dict[str(i)][str(j)][m][0]:
                        if val > 0.001: #ensure minimum bwd available
                            temp = 1/val
                            bwd_cost.append(round(temp, 15))
                        else:
                            bwd_cost.append(1/0.001)
                    paths_metrics_dict[str(i)][str(j)][m][0] = bwd_cost
                met_list = paths_metrics_dict[str(i)][str(j)][m]
                met_norm = [normalize(met_val, 0, 100, min(paths_metrics_dict[str(i)][str(j)][m][0]), max(paths_metrics_dict[str(i)][str(j)][m][0])) for met_val in paths_metrics_dict[str(i)][str(j)][m][0]]
                paths_metrics_dict[str(i)][str(j)][m].append(met_norm)
    
    for i in paths_metrics_dict:
        for j in paths_metrics_dict[i]:
            rewards_actions = []              
            for act in range(20):
                rewards_actions.append(reward(i,j,paths_metrics_dict,act,metrics))
                rewards_dic[i][j] = rewards_actions

    return rewards_dic

def normalize(value, minD, maxD, min_val, max_val):
    if max_val == min_val:
        value_n = (maxD + minD) / 2 
    else:
        value_n = (maxD - minD) * (value - min_val) / (max_val - min_val) + minD
    return round(value_n,15)

def reward(src, dst, paths_metrics_dict, act, metrics):
    '''
    paths_metrics_dict ={src:{dst:{metric1:[[orig value list],[normalized value list]]},metric2...}}
    '''
    beta1=1
    beta2=1
    beta3=1
    cost_action=1
    reward = cost_action + beta1*paths_metrics_dict[str(src)][str(dst)][metrics[0]][1][act] + beta2*paths_metrics_dict[str(src)][str(dst)][metrics[1]][1][act] + beta3*paths_metrics_dict[str(src)][str(dst)][metrics[2]][1][act]
    return round(reward,15)

def check_reward():
    reward = path_metrics_to_reward()
    file = './Routing/1_2.json'
    paths = []
    with open(file,'r') as json_file:
        paths = json.load(json_file)
    for i in range(20):
        print(i,"\t",reward['1']['2'][i],"\t",paths["1"]["2"][i])

if __name__  == '__main__':

    print("Check reward  --> 1\nDRL thread  --> 2")
    i = input()
    if i == str(1):
        check_reward()
    else:
        thread()
