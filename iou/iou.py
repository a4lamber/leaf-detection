'''
 # @ Author: Your name
 # @ Create Time: 2023-03-24 11:18:40
 # @ Modified by: Your name
 # @ Modified time: 2023-03-24 11:18:45
 # @ Description: implementation of IoU
 '''

import torch

def intersection_over_union(boxes_preds,boxes_labels):
    # boxes_pred shape is (N, 4) where N is the # of bboxes
    # boxes_labels is (N,4)
    
    # slicing the tensor shape to be (N,1)
    box1_x1 = boxes_preds[...,0:1]
    box1_y1 = boxes_preds[...,1:2]
    box1_x2 = boxes_preds[...,2:3]
    box1_y2 = boxes_preds[...,3:4]
    box2_x1 = boxes_preds[...,0:1]
    box2_y1 = boxes_preds[...,1:2]
    box2_x2 = boxes_preds[...,2:3]
    box2_y2 = boxes_preds[...,3:4]
    
    x1 = torch.max(box1_x1,box2_x1)
    y1 = torch.max(box1_y1,box2_y1)
    x1 = torch.min(box1_x2,box2_x2)
    y1 = torch.min(box1_y2,box2_y2)
    
    # .clamp(0) is for the case then they do not intersect (edge case)

    


    
