import mlflow
def calculator(a,b,operastion=None):
    if operastion=="add":
        return (a*b)
    elif operastion=="sub":
        return (a-b)
    elif operastion=="mul":
        return (a*b)
    elif operastion=="div":
        return (a/b)

if __name__=="__main__":
    a,b,operation=10454,314046,"div"
    with mlflow.start_run():
        result=calculator(a,b,operation)
        mlflow.log_param("a",a)
        mlflow.log_param("b",b)
        mlflow.log_param("operation",operation)
        mlflow.log_param("result",result)
    
    print(f"my result is {result}")