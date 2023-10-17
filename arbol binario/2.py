#FORMA 2 QUE ME DIJO SAUL QUE ES UN GENIO

def post(preorder, inorder):
    if len(preorder)==0 or len(inorder)==0:
        return ""
    else:
        raiz=preorder[0]
        cont=0
        while (inorder[cont]!=raiz and cont<len(preorder)-1):
            cont=cont+1
        return post(preorder[1:cont+1], inorder[:cont])+post(preorder[cont+1:], inorder[cont+1:])+raiz

if __name__==('__main__'):
    preorder="GEAIBMCLDFKJH"
    inorder="IABEGLDCFMKHJ"
    print(post(preorder,inorder))