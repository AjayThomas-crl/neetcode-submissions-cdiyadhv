class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        if (!strs) {
            return '' 
        }else if (strs[0]==""){
            return ""
        }
        return strs.join('*')
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        if(!str) {
            return []
        }
        return str.split('*')
    }
}
