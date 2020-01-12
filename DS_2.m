function out=DS_2(in,B)
    x1=0;
    x2=0;
    out=zeros(1,length(in));
    for i=1:length(in)
        out(i)=quant(x2,B);
        x1=x1+in(i)-out(i);
        x2=x2+x1-out(i);
    end
end