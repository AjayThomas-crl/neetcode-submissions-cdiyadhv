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
    
    public List<Integer> inorderTraversal(TreeNode root) {
       TreeNode temp=root;
        List<Integer> res=new ArrayList<>();
       inorder(root,res);
        // if root==null
        // res.append(null);
        
        // res.append(root.val)
        // inorder(root.left);
        // // return root.left.val;
        // // return root.right.val;
        // inorder(root.right);
        return res;
    }
    public static void inorder(TreeNode root,List<Integer> res){
       if (root==null){
            
       return;
       }
       inorder(root.left,res);
       System.out.println(root.val);
       res.add(root.val);
       inorder(root.right,res);
       
    }
}