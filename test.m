function out=test(in,B)
    a1=-0.21573658;
    a2=-0.77520416;
    
    b1=-a1;
    b2=0.77520416;
    b3=1;
    
    c1=1;
    c2=1;
    
    d13=0.0008029754470495514;
    e21=0;
    
    out=zeros(1,length(in));
    x1=0;
    x2=0;
    
    for i=1:length(in)
        out(i)=quant((x2*c2)+(in(i)*b3)+(x1*d13),B);
        x2=(x1*c1)+x2+(in(i)*b2)+(out(i)*a2);
        x1=x1+(in(i)*b1)+(out(i)*a1)+(x2*e21);
    end
end

function y=quant(x,B)
    Q=1/(2^(B-1));
    x(x<-1)=-1;
    x(x>1)=1;
    if B==1
        %y = Q*floor(x/Q)+0.5;
        y=sign(x);
    else
        y = Q*floor(x/Q+0.5);
    end
end