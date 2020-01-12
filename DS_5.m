function out=DS_5(in,B)
    x1=0;
    x2=0;
    x3=0;
    x4=0;
    x5=0;
    out=zeros(1,length(in));
    for i=1:length(in)
        out(i)=quant(x5,B);
        x1=x1+in(i)-out(i);
        x2=x2+x1-out(i);
        x3=x3+x2-out(i);
        x4=x4+x3-out(i);
        x5=x5+x4-out(i);
    end
end