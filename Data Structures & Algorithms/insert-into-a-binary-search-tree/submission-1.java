/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode insertIntoBST(TreeNode root, int val) {
        TreeNode temp=root;
        TreeNode prev=new TreeNode();
        
        while(temp!=null){
            prev=temp;
            if(temp.val<val){
                temp=temp.right;
            }else{
                
                temp=temp.left;
            }
           
        }
        TreeNode n=new TreeNode();
        n.val=val;
        if(prev.val<val){
            prev.right=n;
        }else{
            prev.left=n;
        }
        return root;
    }
    
}