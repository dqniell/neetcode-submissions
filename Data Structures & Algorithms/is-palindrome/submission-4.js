class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let l = 0
        let r = s.length - 1

        while (l < r) { 
            if (!isAlphaNumeric(s[l])) { 
                l++; 
            }
            else if (!isAlphaNumeric(s[r])) { 
                r--;  
            }
            else { 
                if (s[l].toLowerCase() !== s[r].toLowerCase()) { 
                    return false; 
                }
                l++; 
                r--; 
            }
        }
        return true; 

        function isAlphaNumeric(c) { 
            return (
                (c >= 'A' && c <= 'Z') ||
                (c >= 'a' && c <= 'z') ||
                (c >= '0' && c <= '9')
            ); 
        }
    }
}
